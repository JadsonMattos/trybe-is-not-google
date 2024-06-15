def exists_word(word, instance):
    result = []
    word = word.lower()
    for i in range(len(instance)):
        file_info = instance.search(i)
        ocorrencias = []
        for j, line in enumerate(file_info['linhas_do_arquivo']):
            if word in line.lower():
                ocorrencias.append({'linha': j + 1})
        if ocorrencias:
            result.append({
                'palavra': word,
                'arquivo': file_info['nome_do_arquivo'],
                'ocorrencias': ocorrencias
            })
    return result


def search_by_word(word, instance):
    result = []
    word = word.lower()
    for i in range(len(instance)):
        file_info = instance.search(i)
        ocorrencias = []
        for j, line in enumerate(file_info['linhas_do_arquivo']):
            if word in line.lower():
                ocorrencias.append({'linha': j + 1, 'conteudo': line})
        if ocorrencias:
            result.append({
                'palavra': word,
                'arquivo': file_info['nome_do_arquivo'],
                'ocorrencias': ocorrencias
            })
    return result
