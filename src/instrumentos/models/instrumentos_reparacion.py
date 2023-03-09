from odoo import models, fields, api

class reparacion(models.Model):
    _name = 'instrumentos.reparacion'
    _description = 'Permite definir unha reparación dun instrumento'
    _order = 'fecha'

    fecha = fields.Date('Fecha', default = fields.date.today())
    tipo = fields.Selection(string = 'Tipo de reparación' , selection = [('l','Limpeza'),('b','Barniz'),('sp','Substitución Pezas'),('o','Outros')], required = True)
    coste = fields.Float('Coste reparación', (6,2), default = 0.0)
    realizada = fields.Boolean('Realizada', default = False)

    instrumento_id = fields.Many2one('instrumentos.instrumento', string = 'Instrumento', required = True)
    #instrumento_ids = fields.Many2many('instrumentos.instrumento', string = 'Instrumentos')
    empleado_id = fields.Many2one('hr.employee', string = 'Empleado')


    def update_reparacionFecha(self):
         self.ensure_one()
         self.fecha = fields.Date.today()

    def update_reparacionRealizada(self):
         self.ensure_one()

         if (self.realizada == True):
              self.realizada = False
         elif (self.realizada == False):
              self.realizada = True