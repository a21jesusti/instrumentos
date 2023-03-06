from odoo import models, fields, api

class instrumento(models.Model):
    _name = 'instrumentos.instrumento'
    _description = 'Permite definir un instrumento'
    _order  = 'name'

    name = fields.Char('Instrumento', required = True)
    marca = fields.Char('Marca', required = True)
    fabricado = fields.Date('Fecha fabricación', default = fields.date.today())
    descripcion  = fields.Text('Descripción', default = 'Información sobre o produto')
    estado = fields.Selection(string='Estado', selection = [('n','Novo'),('r','Reacondicionado'),('a', 'Averiado')],default = 'n', required = True)
    coste = fields.Float('Prezo unidade', (6,1), default = 0.0, required = True)
    costeTotal  = fields.Float('Prezo Total', (9,1), compute = '_get_prezo')
    cantidad = fields.Integer('Cantidade', required = True, default = 0)

    tenda_id = fields.Many2one('instrumentos.tenda', string = 'Tenda', required = True)
    reparacion_ids = fields.Many2many('instrumentos.reparacion', string = 'Reparacións')

    #Creamos o método _get_prezo para o campo computado costeTotal

    @api.depends('estado', 'coste')
    def _get_prezo(self):
        for instrumento in self:
            if instrumento.estado == 'n':
                instrumento.costeTotal = instrumento.coste * instrumento.cantidad
            elif instrumento.estado == 'r':
                instrumento.costeTotal = instrumento.coste * 0.75 * instrumento.cantidad
            elif instrumento.estado == 'a':
                instrumento.costeTotal = 0.0


    #Tratamento dos rexistros por código

    def delete_instrumento(self):
        for instrumento in self:
            instrumento.
        record = self.env['instrumentos.instrumento'].delete()
    
    
    def create_reparacion(self):
        parent_reparacion_val = {
            'tipo': 'b'
        }

        record = self.env['instrumentos.reparacion'].create(parent_reparacion_val)
        return True

    


    