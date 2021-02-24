# -*- coding: utf-8 -*-
from odoo import models, fields, api


class action_So_fields(models.Model):
    _inherit = 'sale.order.line'

    # dyed_fabric

    code_el_loon = fields.Char(string="code_el_loon")
    el_loon = fields.Char(string="el_loon")
    tagheez = fields.Char(string="tagheez")
    al_wazn = fields.Float(string="al_wazn")
    al_3rd = fields.Float(string="al_3rd")
    al_resala = fields.Integer(string="al_resala")
    tasbeet_7rary = fields.Boolean(string="tasbeet_7rary")
    sandy = fields.Boolean(string="sandy")
    mo3alget_zyoot = fields.Boolean(string="mo3alget_zyoot")
    hr2_wabara = fields.Boolean(string="7r2_wabara")
    us_barasel = fields.Boolean(string="us_barasel")
    tasmeegh = fields.Boolean(string="tasmeegh")
    alb_kham = fields.Boolean(string="alb_kham")
    tagheez_compactor = fields.Boolean(string="tagheez_compactor")
    hela2a = fields.Boolean(string="hela2a")
    enzeem = fields.Selection([
        ('enzeem', 'انزيم'),
        ('enzeem_khafeef', 'انزيم خفيف'),
        ('enzeem_motawaset', 'انزيم متوسط'),
        ('enzeem_gayed', 'انزيم جيد'),
        ('enzeem_3aly', 'انزيم عالي'),
        ('enzeem_double', 'انزيم دبل')], string='enzeem')
    kastaraa = fields.Selection([
        ('kastaraa', 'كسترة'),
        ('kastaraa_momtaza', 'كسترة ممتازة'),
        ('kastaraa_3aly', 'كسترة عالية')], string='kastaraa')
    t7deer_7reemy_w_regaly = fields.Selection([
        ('regaly', 'نحضير حريمي'),
        ('7reemy', 'تحضير رجالي')], string='t7deer_7reemy_w_regaly')
    sakhawa = fields.Selection([
        ('sakhawa_3adya', 'سخاوة عادية'),
        ('sakhawa_3alya', 'سخاوة عالية'),
        ('sakhawa_silicon', 'سخاوة ميكروسليكونية')], string='sakhawa')
    ebretan = fields.Selection([
        ('ebretan', 'ابريتان'),
        ('ebretan_double', 'دبل ابريتان')], string='ebretan')

    # GROUP(2)

    strings = fields.Char(string="strings")
    grey_weight = fields.Char(string="grey_weight")
    dyed_weight = fields.Char(string="dyed_weight")
    Width = fields.Char(string="Width")
    machine = fields.Char(string="machine")
    # machine_name = fields.Char(string="machine_name")
    workcenter_id = fields.Many2one('mrp.workcenter', string="Machine Name")
    machine_radiance = fields.Char(string="machine_radiance")
    gouge = fields.Char(string="gouge")
