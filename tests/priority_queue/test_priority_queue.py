from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    pq = PriorityQueue()

    file1 = {"nome_do_arquivo": "file1.txt", "qtd_linhas": 6,
             "linhas_do_arquivo":
             ["line1", "line2", "line3", "line4", "line5", "line6"]}
    file2 = {"nome_do_arquivo": "file2.txt", "qtd_linhas": 4,
             "linhas_do_arquivo": ["line1", "line2", "line3", "line4"]}
    file3 = {"nome_do_arquivo": "file3.txt", "qtd_linhas": 5,
             "linhas_do_arquivo":
             ["line1", "line2", "line3", "line4", "line5"]}

    pq.enqueue(file1)
    pq.enqueue(file2)
    pq.enqueue(file3)

    assert pq.search(0) == file3
    assert pq.search(1) == file2
    assert pq.search(2) == file1
    assert pq.dequeue() == file2
    assert pq.dequeue() == file1
    assert pq.dequeue() == file3
    assert len(pq) == 0
