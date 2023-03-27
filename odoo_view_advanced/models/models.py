# -*- coding: utf-8 -*-
import io
import base64
from odoo import models, fields, api, exceptions


class CustomItem(models.Model):
    _name = 'odoo_view_advanced.custom_item'

    name = fields.Char(string='Descripción')
    unit_price = fields.Char(string='Precio unitario')


class UploadFile(models.TransientModel):
    _name = 'odoo_view_advanced.upload_file'

    upload_file = fields.Binary(string='Subir fichero', required=True)
    file_name = fields.Char(string='Nombre del fichero')

    def import_file(self):
        try:
            if self.file_name:
                if not self.file_name.lower().endswith('.csv'):
                    raise exceptions.ValidationError('El archivo debe ser un CSV')
                file = self.read_file_from_binary(self.upload_file)
                lines = file.split('\n')
                for line in lines:
                    elements = line.split(';')
                    if len(elements) > 1:
                        name = elements[0].strip()
                        unit_price = elements[1].strip()
                        if not name or not unit_price:
                            raise exceptions.ValidationError('El nombre del artículo y el precio unitario son requeridos')
                        self.env['odoo_view_advanced.custom_item'].create({
                            'name': name,
                            'unit_price': float(unit_price)
                        })
        except Exception as e:
            raise exceptions.ValidationError(str(e))

    def read_file_from_binary(self, file):
        try:
            with io.BytesIO(base64.b64decode(file)) as f:
                f.seek(0)
                return f.read().decode('UTF-8')
        except Exception as e:
            raise exceptions.ValidationError(str(e))
