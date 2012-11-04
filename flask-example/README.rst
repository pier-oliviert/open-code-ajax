Démo responsive ajax avec Flask_
================================

Une démo dans la même lignée que @pothibo a fait pour ces apps Django, RoR & Symfony.

.. _Flask: http://flask.pocoo.org/docs/

Installation des dépendances
============================
::
    pip install -r requirements.txt

Création de la base de données
==============================

Dans le commandprompt:

::
    >>> from models import init_db
    >>> init_db()

Démarrer le serveur web de test
===============================
::
    python __init__.py