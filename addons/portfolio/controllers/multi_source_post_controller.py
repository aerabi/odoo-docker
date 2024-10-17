from odoo import http
from odoo.http import request

class MultiSourcePostController(http.Controller):

    @http.route('/issues', auth='public', website=True)
    def list_posts(self, **kwargs):
        # Fetch all posts from the multi_source_post model
        posts = request.env['multi_source_post'].sudo().search([])
        # Render the posts with the corresponding template
        return request.render('portfolio.multi_source_post_template', {'posts': posts})

    @http.route('/issues/<model("multi_source_post"):post>', auth='public', website=True)
    def post_detail(self, post, **kwargs):
        return request.render('portfolio.multi_source_post_detail_template', {'post': post})
