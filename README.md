<p align="center">
  <a title="Documentation" href="https://edaa-org.github.io"><img src="https://img.shields.io/website.svg?label=edaa-org.github.io&longCache=true&style=flat-square&url=http%3A%2F%2Fedaa-org.github.io%2Findex.html&logo=Github&logoColor=fff"></a><!--
  -->
  <a title="'Doc' workflow status" href="https://github.com/edaa-org/edaa-org.github.io/actions?query=workflow%3ADoc"><img alt="'Doc' workflow status" src="https://img.shields.io/github/workflow/status/edaa-org/edaa-org.github.io/Doc/main?longCache=true&style=flat-square&label=Doc&logo=Github%20Actions&logoColor=fff"></a><!--
  -->
  <a title="'Containers' workflow status" href="https://github.com/edaa-org/edaa-org.github.io/actions?query=workflow%3AContainers"><img alt="'Doc' workflow status" src="https://img.shields.io/github/workflow/status/edaa-org/edaa-org.github.io/Containers/main?longCache=true&style=flat-square&label=Containers&logo=Github%20Actions&logoColor=fff"></a><!--
  -->
  <a title="hdl/community on gitter.im" href="https://gitter.im/hdl/community"><img src="https://img.shields.io/gitter/room/hdl/community.svg?longCache=true&style=flat-square&logo=gitter&logoColor=fff&color=4db797"></a><!--
  -->
</p>

# Electronic Design Automation Abstraction (EDA²)

Electronic Design Automation Abstraction (EDA²) is a conceptual model for characterising the abstraction layers in Electronic Design Automation (EDA) projects based on Hardware Description Languages (HDLs).
Its goal is the interoperability of diverse tools and languages, through documented interfaces.

<p align="center">
  <a title="Electronic Design Automation Abstraction (EDA²)" href="https://edaa-org.github.io"><img width="500px" src="_static/logo/edaa_banner_white.svg"/></a>
</p>

EDA² aims to provide reference Python implementations and schemas of commonly needed software layers for (open source) EDA tooling/frameworks to reduce code duplication and reinventions of existing algorithms and data structures.
Each layer solves the problems at a different abstraction level, hence, they are organised accordingly:

<p align="center">
  <a title="Electronic Design Automation Abstraction (EDA²)" href="https://edaa-org.github.io/ConceptualModel.html"><img src="_static/model.png"/></a>
</p>

Although all the resources provided through EDA² can be used together, that is not a requirement.
Third parties are expected to (re)use only the subset of layers that allows them to reduce the maintenance burden of their codebase, while preserving the functionality and UX expected by their user base.
In fact, pyEDAA modules are based on Object Oriented Programming (OOP) patterns, to allow enhancements through inheritance and overriding.

Overall, EDA² provides building blocks to develop GUI solutions such as:

<p align="center">
  <a title="TerosTechnology/vscode-terosHDL GitHub repository" href="https://github.com/TerosTechnology/vscode-terosHDL"><img src="https://img.shields.io/badge/TerosTechnology%2Fvscode-terosHDL-ef5350.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=c62828"></a><!--
  -->
  <a title="umarcor/OSVB GitHub repository" href="https://umarcor.github.io/osvb/apis/project/OSVDE.html"><img src="https://img.shields.io/badge/pyOSVDE-Open%20Source%20VHDL%20Design%20Explorer-ef5350.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=c62828"></a><!--
  -->
</p>

or CLI workflows and tooling:

<p align="center">
  <a title="VUnit/vunit GitHub repository" href="https://github.com/VUnit/vunit"><img src="https://img.shields.io/badge/VUnit-vunit-9ccc65.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=558b2f"></a><!--
  -->
  <a title="Paebbels/pyIPCMI GitHub repository" href="https://github.com/Paebbels/pyIPCMI"><img src="https://img.shields.io/badge/Paebbels-pyIPCMI-9ccc65.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=558b2f"></a><!--
  -->
  <a title="olofk/FuseSoC GitHub repository" href="https://github.com/olofk/FuseSoC"><img src="https://img.shields.io/badge/olofk-FuseSoC-9ccc65.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=558b2f"></a><!--
  -->
  <a title="olofk/Edalize GitHub repository" href="https://github.com/olofk/Edalize"><img src="https://img.shields.io/badge/olofk-Edalize-9ccc65.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=558b2f"></a><!--
  -->
  <a title="tsfpga/tsfpga GitHub repository" href="https://gitlab.com/tsfpga/tsfpga"><img src="https://img.shields.io/badge/tsfpga-tsfpga-9ccc65.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=558b2f"></a><!--
  -->
  <a title="PyFPGA/PyFPGA GitHub repository" href="https://github.com/PyFPGA/PyFPGA"><img src="https://img.shields.io/badge/PyFPGA-PyFPGA-9ccc65.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=558b2f"></a><!--
  -->
  <a title="XedaHQ/Xeda GitHub repository" href="https://github.com/XedaHQ/xeda"><img src="https://img.shields.io/badge/XedaHQ-Xeda-9ccc65.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=558b2f"></a><!--
  -->
  <a title="SymbiFlow/symbiflow-examples GitHub repository" href="https://github.com/SymbiFlow/symbiflow-examples"><img src="https://img.shields.io/badge/SymbiFlow-SymbiFlow--Examples-9ccc65.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=558b2f"></a><!--
  -->
  <a title="cocotb/cocotb GitHub repository" href="https://github.com/cocotb/cocotb"><img src="https://img.shields.io/badge/cocotb-cocotb-9ccc65.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=558b2f"></a><!--
  -->
  <a title="OSVVM/OSVVMLibraries GitHub repository" href="https://github.com/OSVVM/OSVVMLibraries"><img src="https://img.shields.io/badge/OSVVM-OSVVMLibraries-9ccc65.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=558b2f"></a><!--
  -->
  <a title="UVVM/UVVM GitHub repository" href="https://github.com/UVVM/UVVM"><img src="https://img.shields.io/badge/UVVM-UVVM-9ccc65.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=558b2f"></a><!--
  -->
  <a title="HDL/Symbolator GitHub repository" href="https://github.com/HDL/Symbolator"><img src="https://img.shields.io/badge/HDL-Symbolator-9ccc65.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=558b2f"></a><!--
  -->
</p>

That is achieved through a series of tool interfaces:

<p align="center">
  <a title="pyTooling/pyTooling.CLIAbstraction GitHub repository" href="https://github.com/pyTooling/pyTooling.CLIAbstraction"><img src="https://img.shields.io/badge/pyTooling-CLIAbstraction-ffca28.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=ff8f00"></a><!--
  -->
  <a title="edaa-org/pyEDAA.CLITool GitHub repository" href="https://github.com/edaa-org/pyEDAA.CLITool"><img src="https://img.shields.io/badge/pyEDAA-CLITool-ffca28.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=ff8f00"></a><!--
  -->
  <a title="edaa-org/pyEDAA.OutputFilter GitHub repository" href="https://github.com/edaa-org/pyEDAA.OutputFilter"><img src="https://img.shields.io/badge/pyEDAA-OutputFilter-ffca28.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=ff8f00"></a><!--
  -->
</p>

along with syntax/document object models for language and specifications:

<p align="center">
  <a title="VHDL/pyVHDLModel GitHub repository" href="https://github.com/VHDL/pyVHDLModel"><img src="https://img.shields.io/badge/VHDL-pyVHDLModel-29b6f6.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=0277bd"></a><!--
  -->
  <a title="edaa-org/pySVModel GitHub repository" href="https://github.com/edaa-org/pySVModel"><img src="https://img.shields.io/badge/pyEDAA-pySVModel-29b6f6.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=0277bd"></a><!--
  -->
  <a title="edaa-org/pyEDAA.UCIS GitHub repository" href="https://github.com/edaa-org/pyEDAA.UCIS"><img src="https://img.shields.io/badge/pyEDAA-UCIS-29b6f6.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=0277bd"></a><!--
  -->
  <a title="edaa-org/pyEDAA.Reports GitHub repository" href="https://github.com/edaa-org/pyEDAA.Reports"><img src="https://img.shields.io/badge/pyEDAA-Reports-29b6f6.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=0277bd"></a><!--
  -->
</p>

and project abstractions with matching configuration file formats:

<p align="center">
  <a title="edaa-org/pyEDAA.ProjectModel GitHub repository" href="https://github.com/edaa-org/pyEDAA.ProjectModel"><img src="https://img.shields.io/badge/pyEDAA-ProjectModel-ab47bc.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=6a1b9a"></a><!--
  -->
</p>

The end goal is to close the gaps between existing tool, project and HDL source management solutions;
to ease the usage of common and not-so-popular tools in the EDA industry:

<p align="center">
  <a title="gtkwave/gtkwave GitHub repository" href="https://github.com/gtkwave/gtkwave"><img src="https://img.shields.io/badge/gtkwave-gtkwave-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"></a><!--
  -->
  <a title="ghdl/ghdl GitHub repository" href="https://github.com/ghdl/ghdl"><img src="https://img.shields.io/badge/ghdl-ghdl-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"></a><!--
  -->
  <a title="verilator/verilator GitHub repository" href="https://github.com/verilator/verilator"><img src="https://img.shields.io/badge/verilator-verilator-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"></a><!--
  -->
  <a title="steveicarus/iverilog GitHub repository" href="https://github.com/steveicarus/iverilog"><img src="https://img.shields.io/badge/steveicarus-iverilog-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"></a><!--
  -->
  <a title="YosysHQ/yosys GitHub repository" href="https://github.com/YosysHQ/yosys"><img src="https://img.shields.io/badge/YosysHQ-yosys-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"></a><!--
  -->
  <a title="YosysHQ/nextpnr GitHub repository" href="https://github.com/YosysHQ/nextpnr"><img src="https://img.shields.io/badge/YosysHQ-nextpnr-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"></a><!--
  -->
  <a title="YosysHQ/SymbiYosys GitHub repository" href="https://github.com/YosysHQ/SymbiYosys"><img src="https://img.shields.io/badge/YosysHQ-SymbiYosys-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"></a><!--
  -->
  <a title="verilog-to-routing/vtr-verilog-to-routing GitHub repository" href="https://github.com/verilog-to-routing/vtr-verilog-to-routing"><img src="https://img.shields.io/badge/verilog--to--routing-vtr--verilog--to--routing-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"></a><!--
  -->
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Xilinx-ISE-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"><!--
  -->
  <img src="https://img.shields.io/badge/Xilinx-Vivado-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"><!--
  -->
  <img src="https://img.shields.io/badge/Inteal%2FAltera-Quartus-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"><!--
  -->
  <img src="https://img.shields.io/badge/Aldec-ActiveHDL-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"><!--
  -->
  <img src="https://img.shields.io/badge/Aldec-RivieraPRO-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"><!--
  -->
  <img src="https://img.shields.io/badge/Siemens%2FMentor%20Graphics-ModelSim-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"><!--
  -->
  <img src="https://img.shields.io/badge/Siemens%2FMentor%20Graphics-QuestaSim-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"><!--
  -->
  <img src="https://img.shields.io/badge/Lattice-Diamond-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"><!--
  -->
  <img src="https://img.shields.io/badge/Lattice-Radiant-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"><!--
  -->
  <img src="https://img.shields.io/badge/Synopsys-Synplify-78909c.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=37474f"><!--
  -->
</p>
