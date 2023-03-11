from odoo import models, fields, api
from odoo.exceptions import ValidationError



class tenda(models.Model):
    _name = "instrumentos.tenda"
    _description = "Permite definir as características dunha tenda"

    name = fields.Char('Nome', required = True)
    direccion = fields.Text('Direccion', required = True)
    telefono = fields.Char('Teléfono contacto')
    
    instrumento_ids = fields.Many2many('instrumentos.instrumento', string = 'Instrumentos')
    empleado_ids = fields.One2many('hr.employee', 'tenda_id', string = 'Empleados')

    #Tratamento dos rexistros por código

    def create_instrumento(self):

        parent_instrumento_val = {
            'name': 'Proba Instrumento',
            'marca': 'Marca',
            'tenda_ids': [self.env.context.get('active_id')]   
        }
        record = self.env['instrumentos.instrumento'].create(parent_instrumento_val)
        return True
    

    def delete_tenda(self):
        self.ensure_one()
        self.unlink()

    def delete_instrumentos(self):
        for tenda in self:
            tenda.instrumento_ids = [(5,0,0,0,0,0,0,0,0)]
    
