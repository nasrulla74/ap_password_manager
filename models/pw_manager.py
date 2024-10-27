# -*- coding: utf-8 -*-
from odoo import models, fields, api
import cryptocode


secret = "nasrulla1304"
def encrypt(password, secret):
    return cryptocode.encrypt(password,secret)


def decrypt(password, secret):
    return cryptocode.decrypt(password,secret)



class PasswordManager(models.Model):
    _name = "ap.pw.manager"
    _description = "Password Manager"

    name = fields.Char(string="Name", required=True, index=True)
    user_id = fields.Many2one('res.partner', string="Company/User Id", index=True)
    url = fields.Char(string="URL", index=True )
    access_code = fields.Char(string="Access Code", index=True)
    user_name = fields.Char(string="User Name", index=True)
    password = fields.Char(string="Password")
    password_hash = fields.Char(string="Password Hash") # deprecated
    profile_name = fields.Char(string="Profile Name")

    @api.model
    def create(self, vals):
        if 'password' in vals:
            vals['password'] = encrypt(vals['password'], secret)
        return super(PasswordManager, self).create(vals)

    def write(self, vals):
        if 'password' in vals:
            vals['password'] = encrypt(vals['password'], secret)
        return super(PasswordManager, self).write(vals)

    def action_copy_decrypted_text_old(self):
        # Get the decrypted text
        print(self.password, 'pass')
        decrypted_text = decrypt(self.password, secret)
        return {
            'type': 'ir.actions.client',
            'tag': 'copy_decrypted_text',  # This tag needs to be defined in JS
            'params': {'decrypted_text': decrypted_text},
        }


    def action_copy_decrypted_text(self):
        # Get the decrypted text

        self.password_hash = decrypt(self.password, secret)
        print(self.password_hash, 'passddddddddddddddddddddddd')




