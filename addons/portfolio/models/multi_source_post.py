from odoo import models, fields


class MultiSourcePost(models.Model):
    _name = 'multi_source_post'
    _description = 'Multi-source Post'

    title = fields.Char('Title', required=True)
    subtitle = fields.Char('Subtitle')
    content = fields.Html('Content')
    image = fields.Binary('Image', attachment=True)

    # Add links to the alternative versions of the post on other websites
    link_medium = fields.Char('Link_Medium')
    link_twitter = fields.Char('Link_Twitter')
    link_linkedin = fields.Char('Link_Linkedin')
    link_devto = fields.Char('Link_Devto')
    link_other = fields.Char('Link_Other')
