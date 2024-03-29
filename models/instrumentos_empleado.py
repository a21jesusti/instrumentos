from odoo import models, fields, api

class empleado(models.Model):
    _inherit = 'hr.employee'
    
    direccion = fields.Text('Direccion', related='tenda_id.direccion')

    # X Empleados traballan 1 tenda
    tenda_id = fields.Many2one('instrumentos.tenda', string = 'Tenda')
    # Un empleado pode facer N reparacións
    reparacion_ids = fields.One2many('instrumentos.reparacion', 'empleado_id', string = 'Reparacións a cargo')

