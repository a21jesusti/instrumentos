from odoo import models, fields, api

class reparacion(models.Model):
    _name = 'instrumentos.reparacion'
    _description = 'Permite definir unha reparación dun instrumento'
    _order = 'fecha'

    fecha = fields.Date('Fecha', default = fields.date.today())
    tipo = fields.Selection(string = 'Tipo de reparación' , selection = [('l','Limpeza'),('b','Barniz'),('sp','Substitución Pezas'),('o','Outros')], required = True)
    coste = fields.Float('Coste reparación', (6,2), default = 0.0)

    instrumento_ids = fields.Many2many('instrumentos.instrumento', string = 'Instrumentos')
    empleado_id = fields.Many2one('hr.employee', string = 'Empleado')