# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class academy(models.Model):
#     _name = 'academy.academy'
#  
#     name = fields.Char()
    
    
class academy(models.Model):
    _name = 'academy.academy'

    
    name = fields.Char()
    biography = fields.Html()  
    
   # course_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")
   
    course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")
    
class Courses(models.Model):
    _inherit = 'product.template'

    teacher_id = fields.Many2one('academy.teachers', string="Teacher")
    
#   _name = 'academy.courses'
#   _inherit = 'mail.thread'
# name = fields.Char()
  
    