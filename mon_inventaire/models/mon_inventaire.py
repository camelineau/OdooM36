#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Materiel(models.Model):
    _name = 'mon_inventaire.materiel'
    _description = 'mon_inventaire.materiel'

    name = fields.Char(string="Nom du matériel", required = True)
    type = fields.Selection([('Switch', 'SWITCH'),('Routeur', 'ROUTEUR')])
    marque_id = fields.Many2one('mon_inventaire.marque', string='Marque')
    description = fields.Text('Liste du matériel')
    responsable_id = fields.Many2one('mon_inventaire.responsable', string='Responsable')
    responsable_id_full_name = fields.Char(related = 'responsable_id.full_name')

class Marque(models.Model):
    _name = 'mon_inventaire.marque'
    _description = 'mon_inventaire.marque'
    
    name = fields.Char(string="Nom de la marque", required = True)
    materiel_ids = fields.One2many('mon_inventaire.materiel', 'marque_id', string='Matériel associé')
    description = fields.Text()
    
class Responsable(models.Model):
    _name = 'mon_inventaire.responsable'
    _description = 'mon_inventaire.responsable'
    
    name = fields.Char(string="Nom", required = True)
    first_name = fields.Char(string="Prénom", required = True)
    full_name = fields.Char(string = "Responsable", compute="_compute_name", store=True)
    email = fields.Char(string="Email")
    num = fields.Char(string="Numéro de téléphone")
    materiel_ids = fields.One2many('mon_inventaire.materiel', 'responsable_id', string='Matériel')
    materiel_ids_name = fields.Char(related = 'materiel_ids.name')
    
    @api.depends('name','first_name')
    def _compute_name(self):
        for rec in self:
            if rec.name and rec.first_name:
                rec.full_name = rec.name + ' ' + rec.first_name
    