// Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2020.1 (win64) Build 2902540 Wed May 27 19:54:49 MDT 2020
// Date        : Wed Jun 25 12:20:28 2025
// Host        : DESKTOP-UHUOE6D running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode synth_stub
//               d:/Xilinx/Project_NR/again/hw.srcs/sources_1/bd/system/ip/system_DVIClocking_0_0/system_DVIClocking_0_0_stub.v
// Design      : system_DVIClocking_0_0
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7z020clg400-1
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
(* x_core_info = "DVIClocking,Vivado 2020.1" *)
module system_DVIClocking_0_0(PixelClk5X, PixelClk, SerialClk, aLockedIn, 
  aLockedOut)
/* synthesis syn_black_box black_box_pad_pin="PixelClk5X,PixelClk,SerialClk,aLockedIn,aLockedOut" */;
  input PixelClk5X;
  output PixelClk;
  output SerialClk;
  input aLockedIn;
  output aLockedOut;
endmodule
