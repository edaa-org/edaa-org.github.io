.. _EDAA:

.. |SHIELD:svg:repo| image:: https://img.shields.io/github/stars/edaa-org/edaa-org.github.io?longCache=true&style=flat-square&label=edaa-org&logo=github&color=78909c
   :alt: Sourcecode on GitHub
   :height: 22
   :target: https://github.com/edaa-org/edaa-org.github.io

.. |SHIELD:svg:gitter| image:: https://img.shields.io/gitter/room/hdl/community.svg?longCache=true&style=flat-square&logo=gitter&logoColor=fff&color=4db797
   :alt: Chat on Gitter
   :height: 22
   :target: https://gitter.im/hdl/community

.. |shieldgitter| image:: https://img.shields.io/gitter/room/hdl/community.svg?longCache=true&style=flat-square&logo=gitter&logoColor=fff&color=4db797
.. _shieldgitter: https://gitter.im/hdl/community

.. only:: html

    .. centered:: |SHIELD:svg:repo| · |SHIELD:svg:gitter|

    ----

Electronic Design Automation Abstraction (EDA²) Documentation
#############################################################

.. image:: _static/logo/edaa_banner.svg
   :width: 500 px
   :align: center
   :target: https://github.com/edaa-org

.. raw:: html

    <br>

Electronic Design Automation Abstraction (EDA²) is a conceptual model for characterising the abstraction layers in
Electronic Design Automation (EDA) projects based on Hardware Description Languages (HDLs).
Its goal is the interoperability of diverse tools and languages, through documented interfaces.

EDA² aims to provide reference Python implementations and schemas of commonly needed software layers for (open source)
EDA tooling/frameworks to reduce code duplication and reinventions of existing algorithms and data structures.
Each layer solves the problems at a different abstraction level, hence, they are organised as an stack (see :ref:`EDAA:Concept`).

.. image:: _static/model.png
   :width: 500 px
   :align: center
   :target: https://edaa-org.github.io/ConceptualModel.html

.. raw:: html

    <br>

Although all the resources provided through EDA² can be used together, that is not a requirement.
Third-parties are expected to (re)use only the subset of layers that allows them to reduce the maintenance burden of
their codebase, while preserving the functionality and UX expected by their user base.
In fact, pyEDAA modules are based on Object Oriented Programming (OOP) patterns, to allow enhancements through
inheritance and overriding.

Overall, EDA² provides building blocks to develop GUI solutions or CLI workflows and tooling.
That is achieved through a series of tool interfaces, along with syntax/document object models for language and data
format specifications, and project abstractions with matching configuration file formats.
The end goal is to close the gaps between existing tool, project and HDL source management solutions; to ease the usage
of common and not-so-popular tools in the EDA industry.

.. toctree::
   :caption: Introduction
   :maxdepth: 1

   ConceptualModel
   Context
   FAQ

.. toctree::
   :caption: Layers
   :maxdepth: 1

   Configurations
   SyntaxModels
   workflows/index
   CLI

.. toctree::
   :caption: Development

   Status

.. toctree::
   :caption: Appendix
   :maxdepth: 1

   References
