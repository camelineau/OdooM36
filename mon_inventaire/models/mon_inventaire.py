#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Materiel(models.Model):
    _name = 'mon_inventaire.materiel'
    _description = 'mon_inventaire.materiel'

    name = fields.Char(string="Nom du matériel", required = True)
    type = fields.Selection([('Switch', 'SWITCH'),('Routeur', 'ROUTEUR')])
    marque_id = fields.Many2one('mon_inventaire.marque', string='Marque')
    description = fields.Text('Liste du matériel')

class Marque(models.Model):
    _name = 'mon_inventaire.marque'
    _description = 'mon_inventaire.marque'
    
    name = fields.Char(string="Nom de la marque", required = True)
    materiel_ids = fields.One2many('mon_inventaire.materiel', 'marque_id', string='Modèle associé')
    description = fields.Text()
    