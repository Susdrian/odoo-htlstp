import logging
import os

import requests
from odoo import models, api
from dotenv import load_dotenv

_logger = logging.getLogger(__name__)

load_dotenv()

class ExternalDataFetcher(models.AbstractModel):
    _name = 'external.data.fetcher'
    _description = 'External Data Fetcher'

    def _get_header(self):
        odoo_token = os.getenv('ODOO_TOKEN')
        return {
            'Odoo-Token': odoo_token
        }

    @api.model
    def get_customer_data(self, user_id):
        # REPLACE URL
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        header = self._get_header()
        response = requests.get(url, header).headers()
        if response.status_code == 200:
            self.process_customer_data(response.json())
        else:
            _logger.error('Error fetching user data from external API')
            return False

    def process_customer_data(self, data):
        for customer in data:
            self.env['res.partner'].create({
                'name': customer.get('name'),
                'email': customer.get('email'),
                'phone': customer.get('phone'),
            })

    @api.model
    def get_license_details_from_user(self, user_id):
        url = 'https://jsonplaceholder.typicode.com/posts/{}'.format(user_id)
        header = self._get_header()
        response = requests.get(url, header).headers()
        if response.status_code == 200:
            self.process_license_data(response.json())
        else:
            _logger.error('Error fetching license data from external API')
            return False

    def process_license_data(self, data):
        for license in data:
            self.env['asset.asset'].create({
                'license_product': license.get('name'),
                'license_count': license.get('license_count'),
                'license_duration': license.get('license_duration'),
                'user_assignment': license.get('user_assignment'),
                'name': license.get('name'),
                'description': license.get('description'),
                'asset_type': license.get('asset_type'),
            })