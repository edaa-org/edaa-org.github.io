.. _EDAA:Concept:

Conceptual Model
################

EDA² is a conceptual model for characterising the abstraction layers in Electronic Design Automation projects based on
Hardware Description Languages (HDLs).
Its goal is the interoperability of diverse tools and languages with documented APIs.

.. IMPORTANT::
  This conceptual model is not meant to be an isolated full-stack, but each of the layers is to be useful and (re)usable.
  In fact, it is still being enhanced and reworked, so the naming and specific scope of the layers should be taken with
  a grain of salt.

.. figure:: _static/model.png
   :alt: Abstraction layers.
   :align: center
   :width: 600px

   Layers of the EDA² conceptual model.

-1 | Tools
    Development of (open source) EDA tools.
    Organisation `github.com/hdl <https://github.com/hdl>`__ contains an *awesome* list of tools: `hdl.github.io/awesome <https://hdl.github.io/awesome>`__.
    Most EDA tools are developed and managed independently of EDA².
    However, since the main purpose of EDA² is easing the usage of tools, this layer represents them.

0 | Installation
    Packaging and distribution of EDA tools.
    Organisation `github.com/hdl <https://github.com/hdl>`__ contains an index of packaging solutions (`hdl/packages <https://github.com/hdl/packages>`__),
    along with `hdl/smoke-tests <https://github.com/hdl/smoke-tests>`__ for packagers to test the artifacts.
    This layer includes the abstraction(s) for dealing with multiple versions of the tools installed in different
    locations.

1 | CLI
    Abstraction of Command-Line Interface programs (independent of EDA tools).
    May include the abstraction for running isolated tools on containers (e.g. from `hdl/containers <https://github.com/hdl/containers>`__).

2 | EDA
    Interaction with EDA tools (both open source and vendors), including multiple version support, output
    filtering, etc.
    See :ref:`OSVB: Logging <OSVB:API:Logging>`.

3 | Workflows
    Middle layer to translate projects into execution steps (EDA and/or CLI).
    See :ref:`OSVB: Tool <OSVB:API:Tool>` and :ref:`OSVB: Runner <OSVB:API:Runner>`.

4 | Language Model
    Syntax and Document Object Model (DOM) of the imperative and parallel language(s) such as VHDL and System Verilog.
    See:

    * :doc:`vhdlmodel:index`
    * :doc:`svmodel:index`
    * :ref:`OSVB: pyVHDLModelUtils <OSVB:API:Project:pyVHDLModelUtils>`.

5 | Data Model
    IP-XACT, UCIS, XUnit, Cobertura,... imported from or exported into structured files such as JSON, XML, TOML/INI, YAML,...
    See:

    * `pyEDAA.Reports <https://github.com/edaa-org/pyEDAA.Reports>`__
    * `pyEDAA.IPXACT <https://github.com/edaa-org/pyEDAA.IPXACT>`__
    * :ref:`OSVB: Logging <OSVB:API:Logging:OSVR>`

6 | Project Model
    Tool independent information (files/filesets, primary design units, testbenches, `hdl/constraints <https://github.com/hdl/constraints>`__,
    etc.) and tool specific parameters. See :doc:`projectmodel:index`.

7 | Configuration
    INI/JSON/YAML format for providing the sources and constraints data used in Workflow and/or Project through files,
    instead of using the APIs.
    See :ref:`OSVB: Core <OSVB:API:Core>`.

8 | Web
    Web API wrapping the previous layers.

9 | GUI
    Visual frontend to the web API or to the previous layers.
    See :ref:`OSVB: Open Source VHDL Design Explorer (OSVDE) <OSVB:API:Project:OSVDE>`.
