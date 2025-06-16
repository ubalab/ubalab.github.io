#!/usr/bin/python3
import os

# Manually create the first batch of 50 files based on the user's list
# (In a real scenario, this list would be programmatically generated)
files_to_process = [
    "./bloge4a7.html",
    "./blog/em-duas-rodas.html",
    "./blog/experimentacao-transdisciplinar-na-cigac.html",
    "./blog/festa-da-jucara.html",
    "./blog/festival-tropixel.html",
    "./blog/outros-futuros.html",
    "./blog/rio-lixo-montanhas.html",
    "./blog/lixo-eletronico.html",
    "./blog/cursos-pronatec-em-ubatuba.html",
    "./blog/sesi-cultura-digital.html",
    "./blog/encontrao-hipertropical-de-metareciclagem.html",
    "./blog/debate-sobre-o-sistema-nacional-de-cultura.html",
    "./blog/encontrao-hipertropical-engrenagens-em-movimento.html",
    "./blog/outros-lugares.html",
    "./blog/transparencia-e-controle-social.html",
    "./blog/ciclofaixas-sinalizadas.html",
    "./blog/virada-digital.html",
    "./blog/grupo-de-estudos-ubalab.html",
    "./blog/semana-tecnologica-da-etec.html",
    "./blog/geografia-experimental.html",
    "./blog/fortaleza.html",
    "./blog/marin-chamada-aberta.html",
    "./blog/editando-mapas.html",
    "./blog/entrevista-para-revista-rede.html",
    "./blog/e-lento.html",
    "./blog/video-casa-da-cultura-digital.html",
    "./blog/biopunk.html",
    "./blog/tecnologia-por-que-mesmo.html",
    "./blog/profetas-da-chuva.html",
    "./blog/primeira-chamada-encontrao-hipertropical-de-metareciclagem.html",
    "./blog/metareciclando-cidades-digitais.html",
    "./blog/simap-ln.html",
    "./blog/ponto-ubalab.html",
    "./blog/refatorando.html",
    "./blog/acelerando.html",
    "./blog/ipema.html",
    "./blog/energia-pedaletrica.html",
    "./blog/grupo-de-estudos.html",
    "./blog/del-rigor-en-la-ciencia.html",
    "./blog/ubalab-polo-de-tecnologias-livres-status.html",
    "./blog/transparencia-opacidade.html",
    "./blog/do-alto.html",
    "./blog/mudar-ubatuba.html",
    "./blog/bi-ciclos.html",
    "./blog/cidade-expandida.html",
    "./blog/quilombo-da-fazenda.html",
    "./blog/mata-atlantica-no-litoral-norte.html",
    "./blog/o-encontrao-hipertropical-de-metareciclagem.html",
    "./blog/lugares.html",
    "./blog/ao-norte.html"
]

replacements = {
    "http://cdn.jsdelivr.net/bootswatch/3.3.7/yeti/bootstrap.css": "https://cdn.jsdelivr.net/bootswatch/3.3.7/yeti/bootstrap.css",
    "http://code.jquery.com/jquery-1.9.1.js": "https://code.jquery.com/jquery-1.9.1.js",
    "http://cdn.jsdelivr.net/bootstrap/3.3.7/js/bootstrap.js": "https://cdn.jsdelivr.net/bootstrap/3.3.7/js/bootstrap.js"
}

updated_files_count = 0
processed_files_count = 0

print(f"Starting mixed content update for batch of {len(files_to_process)} files.")

for filepath in files_to_process:
    processed_files_count += 1
    if not os.path.exists(filepath):
        print(f"SKIPPING (not found): {filepath}")
        continue

    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as file: # Added errors='replace' for robustness
            content = file.read()
    except Exception as e:
        print(f"ERROR reading {filepath}: {e}")
        continue

    original_content_len = len(content) # Store length for comparison, as content itself can be huge
    modified_content = content

    for old_url, new_url in replacements.items():
        modified_content = modified_content.replace(old_url, new_url)

    if len(modified_content) != original_content_len or modified_content != content : # Check if actual change occurred
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(modified_content)
            print(f"UPDATED (mixed content): {filepath}")
            updated_files_count +=1
        except Exception as e:
            print(f"ERROR writing {filepath}: {e}")
    #else:
        #print(f"No changes needed for (mixed content): {filepath}") # Reducing verbosity

print(f"Mixed content update for batch complete. Processed: {processed_files_count}, Updated: {updated_files_count}")
