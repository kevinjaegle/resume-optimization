import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API-Key sicher einfügen
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print(
        "Warnung: OPENAI_API_KEY ist nicht gesetzt. Bitte füge ihn zu den Umgebungsvariablen oder zur .env Datei hinzu."
    )
else:
    openai.api_key = api_key

    # Lebenslauf und Stellenbeschreibung definieren
    md_resume = """
    # Kevin Jägle

    **Berufsbezeichnung:** DevOps Engineer  
    **E-Mail:** kevinjaegle@outlook.de  
    **Telefon:** +49 15758178224  
    **Adresse:** 77716 Fischerbach  

    ## Über Mich
    Junior DevOps Engineer mit Erfahrung in Containerisierung, Automatisierung und Cloud-Technologien. Spezialisiert auf CI/CD-Pipelines und Blockchain-Technologien.

    ## Berufserfahrung

    ### DevOps Engineer - BAMF, Projekt FLORA
    *Februar 2023 - Februar 2024*  
    - Entwicklung und Wartung von Jenkins-Pipelines und Ansible Playbooks für CI/CD-Deployment.
    - Erstellung von ArgoCD-Anwendungen zur Migration von Microservices zu Cloud-Native-Technologien wie OpenShift.
    - Optimierung von Oracle SQL-Datenbankprozessen zur Verbesserung der Datenqualität.
    - Anpassung von Microservices zur Erweiterung des Konfigurationsmanagements in Spring Boot.
    - Beratung zu IT-Sicherheitsstandards und dezentraler Datenverwaltung mittels Blockchain-Technologien.

    ### DevOps Engineer - Bundesdruckerei, Bildung Procurement Services GmbH
    *März 2024 - heute*  
    - Unterstützung beim Neuaufbau der Entwicklungsumgebung.
    - Konfiguration von Netzwerk- und Serversystemen im Hetzner-Netzwerk.
    - Installation und Konfiguration von Betriebssystemen und Diensten auf neu aufgebauten Servern.
    - Durchführung von Netzwerktests zur Sicherstellung der Funktionsfähigkeit und Sicherheit der Server.
    - Rollout neuer Virtualisierungs- und Betriebssystemlösungen zur Verbesserung der Systemleistung und -sicherheit.

    ### Junior DevOps Engineer - Permtech GmbH
    *Februar 2022 - heute*  
    - Erfahrung in Containerisierung, Automatisierung und Konfigurationsplanung.

    ## Schulbildung

    ### Fachinformatiker für Anwendungsentwicklung
    *Procurement Services GmbH*  
    *2019 - 2022*

    ### Realschulabschluss
    *Abendrealschule*  
    *2017 - 2019*

    ## Fähigkeiten
    - **Containerisierung**
    - **Automatisierung**
    - **Konfigurationsplanung**
    - **Cloud-Technologien**
    - **Programmierung**

    ## Projekte
    - **Projekt FLORA**: Entwicklung von CI/CD-Lösungen, Migration von Microservices, Optimierung von Oracle SQL-Datenbanken.
    - **Projekt Bundesdruckerei**: Neuaufbau der Entwicklungsumgebung, Netzwerk- und Serverkonfiguration, Virtualisierungslösungen.
    """

    job_description = """
    Wir suchen einen DevOps Engineer mit fundierten Kenntnissen in CI/CD-Tools (z.B. Jenkins, Ansible), Erfahrung in der Cloud-Technologie, sowie der Fähigkeit zur Optimierung von Netzwerksystemen. Teamarbeit und gute Kommunikationsfähigkeiten sind uns besonders wichtig.
    """

    # Prompt-Vorlage definieren
    prompt = f"""
    Ich habe einen Lebenslauf im Markdown-Format und eine Stellenbeschreibung. Bitte passe meinen Lebenslauf so an, dass er besser zu den Anforderungen der Stelle passt, insbesondere im Hinblick auf die Nutzung von CI/CD-Tools wie Jenkins und Ansible. Verwende dazu Schlüsselwörter und Phrasen aus der Stellenbeschreibung und betone die Erfahrungen und Fähigkeiten, die besonders relevant sind.

    ### Hier ist mein Lebenslauf in Markdown:
    {md_resume}

    ### Hier ist die Stellenbeschreibung:
    {job_description}

    Passe den Lebenslauf an, indem du:
    - Spezifische Erfahrungen mit Jenkins, Ansible und CI/CD hervorhebst.
    - Sicherstellst, dass die Beschreibung meiner Aufgaben besonders gut zu den geforderten Qualifikationen passt.
    - Professionalität und Klarheit beibehältst.
    """

    # API-Aufruf zur Anpassung des Lebenslaufs
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.25,
    )

    # Angepassten Lebenslauf extrahieren
    updated_resume = response["choices"][0]["message"]["content"].strip()

    # Sicherstellen, dass der Ordner output existiert
    output_dir = "../output"
    os.makedirs(output_dir, exist_ok=True)

    # Angepassten Lebenslauf speichern
    output_path = os.path.join(output_dir, "optimized_resume.md")
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(updated_resume)

    # Erfolgsnachricht ausgeben
    print(f"Der angepasste Lebenslauf wurde erfolgreich gespeichert: {output_path}")
