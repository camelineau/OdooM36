# -*- coding: utf-8 -*-

from odoo import models, fields, api


class classe(models.Model):
    _name = 'gestion_alternant.classe'
    _description = 'gestion_alternant.classe'

    name = fields.Char(string="Classe", required = True)
    alternants_ids = fields.One2many('gestion_alternant.alternant', 'classe_id', string='Alternant')

class alternant(models.Model):
    _name = 'gestion_alternant.alternant'
    _description = 'gestion_alternant.alternant'
    
    name = fields.Char(string="Nom", required = True)
    first_name = fields.Char(string="Prénom", required = True)
    full_name = fields.Char(compute="_compute_name")
    email = fields.Char(string="Email")
    classe_id = fields.Many2one('gestion_alternant.classe', string="Classe")
    entreprise_id = fields.Many2one('gestion_alternant.entreprise', string="Entreprise")
    tuteur_entr_id = fields.Many2one('gestion_alternant.tuteur_entr', string="Tuteur d'Entreprise")
    tuteur_entr_id_full_name = fields.Char(related = 'tuteur_entr_id.full_name')
    tuteur_univ_id = fields.Many2one('gestion_alternant.tuteur_univ', string="Tuteur Universitaire")
    tuteur_univ_id_full_name = fields.Char(related = 'tuteur_univ_id.full_name')
    
    @api.depends('name','first_name')
    def _compute_name(self):
        for rec in self:
            rec.full_name = rec.name + ' ' + rec.first_name
    
class entreprise(models.Model):
    _name = 'gestion_alternant.entreprise'
    _description = 'gestion_alternant.entreprise'
    
    name = fields.Char(string="Nom", required = True)
    adresse = fields.Char(string="Adresse", required = True) 
    alternants_ids = fields.One2many('gestion_alternant.alternant', 'entreprise_id', string='Alternant')
    tuteur_ids = fields.One2many('gestion_alternant.tuteur_entr', 'entr_id', string='Tuteur')
    
class tuteur_entr(models.Model):
    _name = 'gestion_alternant.tuteur_entr'
    _description = 'gestion_alternant.tuteur_entr'
    
    name = fields.Char(string="Nom", required = True)
    first_name = fields.Char(string="Prénom", required = True)
    full_name = fields.Char(compute="_compute_name")
    email = fields.Char(string="Email")
    num = fields.Char(string="Numéro de téléphone")
    entr_id = fields.Many2one('gestion_alternant.entreprise', string="Entreprise")
    alternants_ids = fields.One2many('gestion_alternant.alternant', 'tuteur_entr_id', string='Alternant')
    
    @api.depends('name','first_name')
    def _compute_name(self):
        for rec in self:
            rec.full_name = rec.name + ' ' + rec.first_name
    
class tuteur_univ(models.Model):
    _name = 'gestion_alternant.tuteur_univ'
    _description = 'gestion_alternant.tuteur_univ'
    
    name = fields.Char(string="Nom", required = True) 
    first_name = fields.Char(string="Prénom", required = True) 
    full_name = fields.Char(compute="_compute_name")
    email = fields.Char(string="Email")
    num = fields.Char(string="Numéro de téléphone")
    alternants_ids = fields.One2many('gestion_alternant.alternant', 'tuteur_univ_id', string='Alternant')

    @api.depends('name','first_name')
    def _compute_name(self):
        for rec in self:
            rec.full_name = rec.name + ' ' + rec.first_name
    