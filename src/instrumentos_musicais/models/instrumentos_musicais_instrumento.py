from odoo import models, fields, api

class instrumento(models.Model):
    _name = "instrumentos_musicais.instrumento"
    _description = "Permite definir un instrumento"

    name = fields.Char('Instrumento', required = True)
    marca = fields.Char('Marca', required = True)
    fabricado = fields.Date('Fecha fabricación', default = fields.date.today)
    descripcion  = fields.Text('Descripción', default = 'Información sobre o produto')
    estado = fields.Selection(string='Estado', selection = [('n','Novo'),('r','Reacondicionado'),('a', 'Averiado')],default = 'n', required = True)
    coste = fields.Float('Prezo unidade', (6,1), default = 0.0, required = True)
    costeTotal  = fields.Float('Prezo Total', (9,1), compute = '_get_prezo')
    cantidad = fields.Integer('Cantidade', required = True, default = 0)

    @api.depends('estado', 'coste')
    def _get_prezo(self):
        for instrumento in self:
            if instrumento.estado.equals('n'):
                instrumento.costeTotal = instrumento.coste * instrumento.cantidad
            elif instrumento.estado.equals('r'):
                instrumento.costeTotal = instrumento.coste * 0,75 * instrumento.cantidad
            elif instrumento.estado.equals('a'):
                instrumento.costeTotal = 0.0


    


    