Démo responsive ajax avec Flask_
================================

Une démo dans la même lignée que @pothibo a fait pour ces apps Django, RoR & Symfony.

.. _Flask: http://flask.pocoo.org/docs/

Installation et activation de l'environnement de développement
==============================================================

Dans le terminal::

    $ pip install virtualenv
    $ virtualenv venv
    $ . venv/bin/activate

Vous devriez maintenant voir le préfix *(venv)* avant le $.

Installation des dépendances
============================

Dans le terminal::

    $ pip install -r requirements.txt

Création de la base de données
==============================

Dans le terminal::

    $ python
    >>> from models import init_db
    >>> init_db()

Démarrer le serveur web de test
===============================

Dans le terminal::

    $ python __init__.py
