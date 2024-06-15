from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in instance.queue:
        if item['nome_do_arquivo'] == path_file:
            return

    lines = txt_importer(path_file)
    if lines is not None:
        data = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(lines),
            'linhas_do_arquivo': lines
        }
        instance.enqueue(data)
        print(data)


def remove(instance):
    if len(instance) == 0:
        print('Não há elementos')
        return

    removed_file = instance.dequeue()
    print(f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        file_info = instance.search(position)
        print(file_info)
    except IndexError:
        sys.stderr.write('Posição inválida\n')
