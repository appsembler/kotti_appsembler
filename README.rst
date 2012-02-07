Kotti
=====

Edit the ``postgresql-kotti`` entry in stackato.yml to::

    services:
        mysql: postgresql-yourappname

From the ``kotti_appsembler`` directory, deploy with these commands::

    stackato target api.appsembler.com
    stackato login --email name@domain.com --password *****
    stackato push yourappname --url yourappname.appsembler.com -n

Substitute ``yourappname`` with whatever you want to call your Kotti app instance.
Substitute ``name@domain.com`` with your email address.
