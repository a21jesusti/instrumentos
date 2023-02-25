from odoo import models, fields, api

class tenda(models.Model):
    _name = "instrumentos_musicais.tenda"
    _description = "Permite definir as características dunha tenda"

    name = fields.Char('Nome', required = True)
    direccion = fields.Text('Direccion', required = True)
    telefono = fields.Char('Teléfono contacto')

