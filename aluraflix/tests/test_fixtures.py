from django.test import TestCase
from aluraflix.models import Programa


class FixtureDataTestCase(TestCase):
    fixtures = ['programas_iniciais']

    def test_verifica_carregamento_da_fixture(self):
        '''
        Testa o titulo de um programa carregado atraves de um arquivo e
        a quantidade de programas encontrados no arquivo.
        '''
        programa_bizarro = Programa.objects.get(pk=1)
        todos_os_programas = Programa.objects.all()
        self.assertEqual(programa_bizarro.titulo, 'Coisas bizarras')
        self.assertEqual(len(todos_os_programas), 9)
