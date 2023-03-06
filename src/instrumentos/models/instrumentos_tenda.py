from odoo import models, fields, api

class tenda(models.Model):
    _name = "instrumentos.tenda"
    _description = "Permite definir as características dunha tenda"

    name = fields.Char('Nome', required = True)
    direccion = fields.Text('Direccion', required = True)
    telefono = fields.Char('Teléfono contacto')
    
    instrumento_ids = fields.One2many('instrumentos.instrumento', 'tenda_id', string = 'Instrumentos')
    empleado_ids = fields.One2many('hr.employee', 'tenda_id', string = 'Empleados')

    #Tratamento dos rexistros por código

    def create_instrumento(self):
        parent_instrumento_val = {
            'name': 'Proba Instrumento',
            'marca': 'Marca',
            'tenda_id': 1
            
        }
        record = self.env['instrumentos.instrumento'].create(parent_instrumento_val)
        return True