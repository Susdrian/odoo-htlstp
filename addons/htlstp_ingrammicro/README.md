# Ingram Micro
## Required Functions
### Sync Products
Inbound Sync (eg Daily) of Product Articles with a Filter to include or exclude Product Categories.

Requirements:
* It should be possible to select Product Categories (Vendors) which are Synced. Eg Only Sync Products from Microsoft 365.
* Each Product should include the current Reseller Price (Our Cost from Ingram)
* Each Product should be assigned a Retail Price only on first import.
* Possible to Combine Ingram Products with other Products (eg M365 License with an additional Backup License and Phishing Subscription). The Cost should be Updated Daily
* M365 License currently have 3 Options, these should be Reflected the Product name
  * Monthly Payment, Annual Commitment
  * Monthly Payment, Monthly Commitment
  * Annual Payment, Annual Commitment

### Billing Cycle
* Each Month an Invoice is created. The Invoice is created either manually or automatically.
* For Annual Commitment Products a Quote should be created one month before the previous commitment ends or manually triggered.
* If a Quote or an Invoice is created manually no additional Quote or Invoice should be created for the current billing cycle (this is default behavior of odoo subscriptions in odoo atm)
* Each Quote or Invoice should include an overview of the current license assignment. (What license a User has and a count of unassigned licenses)
* the qty of licenses or combined products should only depend on the currently booked licenses. This can be integrated at a later stage with information provided by NinjaRMM or CIPP (M365 Management Tool that offers an API as well)
* The Billing Cycle should be created either during or the current cycle or before the upcoming cycle.
We either charge the next Upcoming Month or the current Month.
We did some changes to the default subscription module that changes the dates visible to the customer to "fake" the subscription date to the current or next full month depending on the Subscription Quote created for the customer.
* It would be nice to have an overview for upcoming renewals of the annual commitments, with a reminder sent by email that an action is required to reduce the license qty at renewal date (maybe daily emails as well until invoice is created or after the invoice is created)

