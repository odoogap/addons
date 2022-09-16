# Object Route

## Overview

Prevent publishing products with MTO and Manufacture routes with no BOM, and products with MTO and Buy routes with no seller and prevent it from being published, and create a filter for these issues.

## Purpose

### Why we decide to provide this module?

This module will create a warning to tell the customer if the MTO and Manufacture routes are selected with no BOM or if the MTO and Buy routes are selected with no seller to avoid failures on Order creation. It will prevent it from publishing these products, and create a filter for these issues.

## Features

* We support both community and enterprise editions
* Currently support version 14.0 , 15.0

## How to install

* Firstly, ensure that the module file is present in the add-ons directory of the Odoo server
* Update Modules list so that it appears in the UI within Apps store
* Update Modules list so that it appears in the UI within Apps
* Look for the module within Apps and click on Install

## How to use

	* Select both MTO and Buy routes with no seller, a warning will pop-up and tell you **This product has no Supplier**. And it will prevent you from publishing this product
	* Select both MTO and Manufacture routes with no BOM, a warning will pop-up and tell you **This product has no BOM**. And it will prevent you from publishing this product
	* Create a filter that contains all these products.

## Support

To report a problem please [contact us](https://www.erpgap.com/page/contactus/).

Commercial support is available, please email [info@erpgap.com](info@erpgap.com)
or call tel:+44 7480 538242 for further information.
