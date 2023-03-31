# -*- coding: utf-8 -*-
import unittest
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from odoo_view_advanced.models import CustomItem, UploadFile


class TestUploadFile(TransactionCase):

    def setUp(self):
        super(TestUploadFile, self).setUp()

    def test_import_file(self):
        # Cargar archivo de prueba
        with open('test_file.csv', 'rb') as f:
            file_content = f.read()
        upload_file = UploadFile.create({
            'upload_file': file_content,
            'file_name': 'test_file.csv'
        })

        # Importar archivo
        upload_file.import_file()

        # Verificar que se crearon los registros correctamente
        self.assertEqual(len(CustomItem.search([])), 3)

        # Importar archivo con un nombre de archivo no válido
        upload_file.file_name = 'test_file.txt'
        with self.assertRaises(ValidationError):
            upload_file.import_file()

        # Importar archivo con una línea vacía
        with open('test_file_with_empty_line.csv', 'rb') as f:
            file_content = f.read()
        upload_file.upload_file = file_content
        upload_file.file_name = 'test_file_with_empty_line.csv'
        with self.assertRaises(ValidationError):
            upload_file.import_file()


if __name__ == '__main__':
    unittest.main()
