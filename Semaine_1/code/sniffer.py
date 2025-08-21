#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sniffer réseau basique en Python (Ubuntu / Linux)
------------------------------------------------
Ce script capture les trames réseau brutes sur une interface spécifique
et affiche les données en hexadécimal + ASCII.

ATTENTION SÉCURITÉ :
- Ce script nécessite des privilèges administrateur (sudo) pour accéder aux raw sockets
- L'utilisation de sniffers réseau doit respecter les lois locales et les politiques d'entreprise
- Ne jamais utiliser sur des réseaux dont vous n'êtes pas propriétaire sans autorisation

CONCEPTS PÉDAGOGIQUES :
- Raw sockets : accès direct aux trames réseau de niveau 2 (couche liaison)
- AF_PACKET : famille de sockets pour accéder aux paquets au niveau Ethernet
- Hexdump : affichage des données binaires en format hexadécimal lisible

L'utilisateur choisit l'interface dans une liste détectée automatiquement.
"""

import socket

# ==========================
# Fonctions utilitaires
# ==========================

def hexdump(data: bytes, length: int = 16) -> str:
    """
    Convertit des données binaires en format hexadécimal lisible.
    
    Cette fonction imite l'affichage de Wireshark ou tcpdump pour visualiser
    le contenu des trames réseau octet par octet.
    
    Args:
        data (bytes): Les données binaires à convertir (contenu d'une trame réseau)
        length (int): Nombre d'octets à afficher par ligne (défaut: 16)
    
    Returns:
        str: Chaîne formatée avec offset, hex et ASCII
        
    Exemple de sortie:
        0000  08 00 27 12 34 56 08 00  27 87 65 43 08 00 45 00  ..'♪4V..'♪eC..E.
        0010  00 3c 1c 46 40 00 40 06  b1 e6 ac 11 00 0c ac 11  .<♪F@.@♪......
    
    Format expliqué:
        - 0000 : offset en hexadécimal (position dans les données)
        - 08 00 27... : données en hexadécimal (2 caractères par octet)
        - ..'♪4V... : représentation ASCII (. si non imprimable)
    """
    result = []
    # Parcourir les données par blocs de 'length' octets
    for i in range(0, len(data), length):
        # Extraire un bloc d'octets
        chunk = data[i:i+length]
        
        # Convertir chaque octet en hexadécimal (format 02x = 2 chiffres avec zéro)
        hex_part = " ".join(f"{b:02x}" for b in chunk)
        
        # Convertir en ASCII (remplacer les caractères non imprimables par '.')
        # ASCII imprimable : codes 32 à 126 (espace à tilde ~)
        ascii_part = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        
        # Formater la ligne : offset + hex (aligné) + ASCII
        result.append(f"{i:04x}  {hex_part:<{length*3}}  {ascii_part}")
    
    return "\n".join(result)

# ==========================
# Programme principal
# ==========================

def main():
    """
    Fonction principale qui gère l'interface utilisateur et la capture de trames.
    
    Étapes du programme :
    1. Lister les interfaces réseau disponibles
    2. Permettre à l'utilisateur de choisir une interface
    3. Créer un raw socket pour capturer les trames
    4. Afficher les trames capturées en continu
    """
    
    # ==== ÉTAPE 1 : Découverte des interfaces réseau ====
    # socket.if_nameindex() retourne une liste de tuples (index, nom_interface)
    # Exemple : [(1, 'lo'), (2, 'eth0'), (3, 'wlan0')]
    interfaces = socket.if_nameindex()
    print("=== Interfaces réseau disponibles ===")
    print("(Note: 'lo' = loopback, 'eth0' = Ethernet, 'wlan0' = WiFi)")
    
    for idx, (_, if_name) in enumerate(interfaces, start=1):
        print(f"{idx}. {if_name}")

    # ==== ÉTAPE 2 : Sélection de l'interface par l'utilisateur ====
    while True:
        try:
            choice = int(input("Choisissez une interface (numéro) : "))
            # Vérifier que le choix est dans la plage valide
            if 1 <= choice <= len(interfaces):
                # Récupérer le nom de l'interface (second élément du tuple)
                interface = interfaces[choice - 1][1]
                break
            else:
                print("Numéro invalide, réessayez.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    print(f"\nInterface sélectionnée : {interface}")

    # ==== ÉTAPE 3 : Création du raw socket ====
    # AF_PACKET : famille de sockets pour accéder aux paquets Ethernet
    # SOCK_RAW : type de socket pour accès direct aux trames brutes
    # 0x0003 : ETH_P_ALL en hexadécimal - capture tous les protocoles
    # socket.ntohs() convertit de l'ordre réseau vers l'ordre hôte
    print("\nCréation du raw socket...")
    print("ATTENTION : Nécessite des privilèges root (sudo)")
    
    try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        print("✓ Raw socket créé avec succès")
    except PermissionError:
        print("❌ Erreur : Privilèges insuffisants. Exécutez avec 'sudo python3 sniffer.py'")
        return
    except OSError as e:
        print(f"❌ Erreur lors de la création du socket : {e}")
        return
    
    # Note : s.bind((interface, 0)) pourrait être utilisé pour lier à une interface spécifique
    # Commenté car le socket capture déjà sur toutes les interfaces par défaut

    print(f"\n=== Capture en cours sur {interface} ===")
    print("Appuyez sur Ctrl+C pour arrêter\n")
    print("Format d'affichage :")
    print("- Taille de la trame en octets")
    print("- Hexdump : offset | données hex | ASCII lisible")
    print("- Séparateur entre trames")
    print()

    # ==== ÉTAPE 4 : Boucle de capture et affichage ====
    try:
        while True:
            # recvfrom(65535) : taille max d'un paquet Ethernet (en pratique ~1500 octets)
            # raw_data : données binaires de la trame complète (en-têtes + payload)
            # addr : adresse source (non utilisée dans ce script éducatif)
            raw_data, _ = s.recvfrom(65535)
            
            print(f"Trame reçue ({len(raw_data)} octets)")
            print(hexdump(raw_data))
            print("-" * 60)

    except KeyboardInterrupt:
        print("\n✓ Arrêt de la capture demandé par l'utilisateur.")
    except Exception as e:
        print(f"\n❌ Erreur durant la capture : {e}")
    finally:
        # Toujours fermer le socket pour libérer les ressources
        s.close()
        print("✓ Socket fermé proprement.")

# ==========================
# Point d'entrée du script
# ==========================

if __name__ == "__main__":
    """
    Point d'entrée du programme.
    
    Le test 'if __name__ == "__main__"' garantit que main() ne s'exécute
    que si le script est lancé directement (pas importé comme module).
    
    UTILISATION :
        sudo python3 sniffer.py
        
    PRÉREQUIS :
        - Système Linux/Ubuntu (utilise AF_PACKET spécifique à Linux)
        - Privilèges administrateur (sudo) pour accéder aux raw sockets
        - Python 3.6+ (pour les f-strings)
        
    APPRENTISSAGE :
        Ce script illustre les concepts fondamentaux de l'analyse réseau :
        - Capture de trames au niveau liaison (Layer 2)
        - Format des données binaires réseau
        - Visualisation hexadécimale des protocoles
        - Programmation socket en mode raw
    """
    main()