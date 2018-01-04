# -*- coding: utf-8 -*-
import re
from odoo import api, fields, models,_
from odoo.exceptions import UserError,ValidationError

class StudentDetails(models.Model):
	_inherit = 'res.partner'

	is_status = fields.Selection(
		[
			('stud','Student'),
			('librarian','Librarian'),
			('author','Author'),
			('publisher','Publisher'),
		],

		default='stud'

		)

	gender = fields.Selection(
		[
			('male','Male'),
			('female','Female'),
			('other','Other')
		])
	divisoin = fields.Selection(
		[
			('1','A'),
			('2','B'),
			('0','Other')
		])
	date = fields.Date("Date")

	@api.onchange('is_status')
	def onchange_standard(self):
		if self.is_status  == 'stud' :
			 self.function  = 'Student'

		elif self.is_status == 'librarian':
			 self.function 	= 	'Librarian'

	@api.constrains('mobile')
	def check_phone_no(self):
		if self.mobile:
			if not self.mobile.isdigit():
				if len(self.mobile)!=10 :
					raise ValidationError(_('Mobile number must be 10 digits numeric!!!'))
		else:
			raise ValidationError(_('Mobile number must be 10 digits numeric!!!'))


		# if re.match("[0-9]{10}",self.mobile)==None:
		# 	raise ValidationError(_('Mobile number must be 10 digits numeric!!!'))
		
	@api.constrains('email')
	def check_email(self):
		EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
		if self.email and not EMAIL_REGEX.match(self.email):		
			raise ValidationError(_('Email id invalid..!'))



	# ./odoo-bin -d asd --db-filter=asd --addons-path=addons,../library-management -u library_management
