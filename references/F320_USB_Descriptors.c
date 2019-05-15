//-----------------------------------------------------------------------------
// F320_USB_Descriptors.c
//-----------------------------------------------------------------------------
// Copyright 2005 Silicon Laboratories, Inc.
// http://www.silabs.com
//
// Program Description:
//
// This is the module contains USB descriptor definitions used for USB
// device enumeration.
//
// FID:            32X000062
// Target:         C8051F320
// Tool chain:     KEIL C51 7.0.0.1 / KEIL A51 7.0.0.1
//                 Silicon Laboratories IDE version 2.3
// Command Line:   See Readme.txt
// Project Name:   F320_DEFAULT
//
// Release 1.0
//    -Initial Revision (PD)
//    -05 JUL 2006
//
//
//-----------------------------------------------------------------------------
// Includes
//-----------------------------------------------------------------------------
#include "c8051f320.h"                 // SFR declarations
#include "F320_USB_Descriptor.h"       // USB descriptor definitions
//-----------------------------------------------------------------------------
// Variable Declaration
//-----------------------------------------------------------------------------
// Descriptor Declarations
code const device_descriptor DeviceDesc =
{0x12, // bLength (18)
 0x01, // bDescriptorType (DEVICE)
 0x1001, // bcdUSB (1.1)
 0x00, // bDeviceClass (none)
 0x00, // bDeviceSubClass (none)
 0x00, // bDeviceProtocol (none)
 EP0_PACKET_SIZE, // bMaxPacketSize0 (64)
 LE(VID), // idVendor
 LE(PID), // idProduct
 0x0001, // bcdDevice (1.0)
 0x01, // iManufacturer (index 1)
 0x02, // iProduct (index 2)
 0x00, // iSerialNumber (none)
 0x01 // bNumConfigurations (1)
 };  // End of DeviceDesc
// This device has one configuration containing 4 total interfaces, three of
// which are active at any one time.
code const complete_configuration ConfigDesc =
{
   {                                   // Standard configuration descriptor
      0x09,                            // bLength (9)
      0x02,                            // bDescriptorType (CONFIGURATION)
      0x9100,                          // wTotallength (145)
      0x03,                            // bNumInterfaces (3)
      0x01,                            // bConfigurationValue (1)
      0x00,                            // iConfiguration (none)
      0x80,                            // bmAttributes (bus-powered)
      0x32,                            // bMaxPower (100 mA)
   },
   {                                   // Audio control interface
      0x09,                            // bLength (9)
      0x04,                            // bDescriptorType (INTERFACE)
      0x00,                            // bInterfaceNumber (0)
      0x00,                            // bAlternateSetting (none)
      0x00,                            // bNumEndpoints (none)
      0x01,                            // bInterfaceClass (AUDIO)
      0x01,                            // bInterfaceSubClass (AUDIO_CONTROL)
      0x00,                            // bInterfaceProtocol (none)
      0x00                             // iInterface (none)
   },
   {                                   // Audio class-specific interface header
      0x09,                            // bLength (9)
      0x24,                            // bDescriptorType (CS_INTERFACE)
      0x01,                            // bDescriptorSubtype (HEADER)
      0x0001,                          // bcdADC (1.0)
      0x2B00,                          // wTotalLength (43)
      0x01,                            // bInCollection (1 streaming interface)
      0x01                             // baInterfaceNr (interface 1 is stream)
   },
   {                                   // Audio class-specific input terminal
      0x0C,                            // bLength (12)
      0x24,                            // bDescriptorType (CS_INTERFACE)
      0x02,                            // bDescriptorSubtype (INPUT_TERMINAL)
      0x01,                            // bTerminalID (1)
      0x1007,                          // wTerminalType (radio receiver)
      0x00,                            // bAssocTerminal (none)
      0x02,                            // bNrChannels (2)
      0x0300,                          // wChannelConfig (left, right)
      0x00,                            // iChannelNames (none)
      0x00                             // iTerminal (none)
   },
   {                                   // Audio class-specific feature unit
      0x0D,                            // bLength (13)
      0x24,                            // bDescriptorType (CS_INTERFACE)
      0x06,                            // bDescriptorSubtype (FEATURE_UNIT)
      0x02,                            // bUnitID (2)
      0x01,                            // bSourceID (input terminal 1)
      0x02,                            // bControlSize (2 bytes)
      0x0100,                          // Master controls
      0x0000,                          // Channel 0 controls
      0x0000,                          // Channel 1 controls
      0x00                             // iFeature (none)
   },
   {                                   // Audio class-specific output terminal
      0x09,                            // bLength (9)
      0x24,                            // bDescriptorType (CS_INTERFACE)
      0x03,                            // bDescriptorSubtype (OUTPUT_TERMINAL)
      0x03,                            // bTerminalID (3)
      0x0101,                          // wTerminalType (USB streaming)
      0x00,                            // bAssocTerminal (none)
      0x02,                            // bSourceID (feature unit 2)
      0x00                             // iTerminal (none)
   },
   {                                   // Audio zero-bandwidth interface
      0x09,                            // bLength (9)
      0x04,                            // bDescriptorType (INTERFACE)
      0x01,                            // bInterfaceNumber (1)
      0x00,                            // bAlternateSetting (0)
      0x00,                            // bNumEndpoints (0)
      0x01,                            // bInterfaceClass (AUDIO)
      0x02,                            // bInterfaceSubClass (AUDIO_STREAMING)
      0x00,                            // bInterfaceProtocol (none)
      0x00                             // iInterface (none)
   },
   {                                   // Audio streaming interface (alternate)
      0x09,                            // bLength (9)
      0x04,                            // bDescriptorType (INTERFACE)
      0x01,                            // bInterfaceNumber (1)
      0x01,                            // bAlternateSetting (1)
      0x01,                            // bNumEndpoints (1)
      0x01,                            // bInterfaceClass (AUDIO)
      0x02,                            // bInterfaceSubClass (AUDIO_STREAMING)
      0x00,                            // bInterfaceProtocol (none)
      0x00                             // iInterface (none)
   },
   {                                   // Audio class-specific stream interface
      0x07,                            // bLength (7)
      0x24,                            // bDescriptorType (CS_INTERFACE)
      0x01,                            // bDescriptorSubtype (AS_GENERAL)
      0x03,                            // bTerminalLink (terminal 3)
      0x00,                            // bDelay (none)
      0x0100                           // wFormatTag (PCM format)
   },
   {                                   // Audio class-specific type I format
      0x0B,                            // bLength (11)
      0x24,                            // bDescriptorType (CS_INTERFACE)
      0x02,                            // bDescriptorSubtype (FORMAT_TYPE)
      0x01,                            // bFormatType (TYPE_I)
      0x02,                            // bNrChannels (2)
      0x02,                            // bSubFrameSize (2)
      // The next field should be 10, but 16 works with more standard software
      0x10,                            // bBitResolution (16)
      0x01,                            // bSamFreqType (1 sampling frequency)
      0x80,                            // 48,000 Hz (byte 0)
      0xBB,                            // 48,000 Hz (byte 1)
      0x00                             // 48,000 Hz (byte 2)
   },
   {                                   // Audio streaming isochronous endpoint
      0x09,                            // bLength (9)
      0x05,                            // bDescriptorType (ENDPOINT)
      0x83,                            // bEndpointAddress (EP3 in)
      0x05,                            // bmAttributes (asynchronous)
      0x0002,                          // wMaxPacketSize (512)
      0x01,                            // bInterval (1 millisecond)
      0x00,                            // bRefresh (0)
      0x00                             // bSynchAddress (no synchronization)
   },
   {                                   // Audio isochronous endpoint
      0x07,                            // bLength (7)
      0x25,                            // bDescriptorType (CS_ENDPOINT)
      0x01,                            // bDescriptorSubtype (EP_GENERAL)
      0x00,                            // bmAttributes (none)
      0x02,                            // bLockDelayUnits (PCM samples)
      0x0000                           // wLockDelay (0)
   },
   {                                   // HID interface
      0x09,                            // bLength (9)
      0x04,                            // bDescriptorType (INTERFACE)
      0x02,                            // bInterfaceNumber (2)
      0x00,                            // bAlternateSetting (0)
      0x02,                            // bNumEndpoints (2)
      0x03,                            // bInterfaceClass (HID)
      0x00,                            // bInterfaceSubClass (none)
      0x00,                            // bInterfaceProtocol (none)
      0x00                             // iInterface (none)
   },
   {                                   // HID descriptor
      0x09,                            // bLength (9)
      0x21,                            // bDescriptorType (HID_DESCRIPTOR)
      0x1101,                          // bcdHID (1.11)
      0x00,                            // bCountryCode (none)
      0x01,                            // bNumDescriptors (1 class descriptor)
      0x22,                            // bClassDescriptorType (report descr.)
      LE(HID_REPORT_SIZE)              // wDescriptorLength (203)
   },
   {                                   // HID interrupt in endpoint
      0x07,                            // bLength (7)
      0x05,                            // bDescriptorType (ENDPOINT)
      0x81,                            // bEndpointAddress (EP1 in)
      0x03,                            // bmAttributes (interrupt)
      0x4000,                          // wMaxPacketSize (64)
      0x0A                             // bInterval (10 milliseconds)
   },
   {                                   // HID interrupt out endpoint
      0x07,                            // bLength (7)
      0x05,                            // bDescriptorType (ENDPOINT)
      0x02,                            // bEndpointAddress (EP2 out)
      0x03,                            // bmAttributes (interrupt)
      0x4000,                          // wMaxPacketSize (64)
      0x01                             // bInterval (1 millisecond)
   }
};                                     // End of ConfigDesc
code const hid_report_descriptor HidReportDesc =
{
   0x06, 0x00, 0xFF,                   // USAGE_PAGE (Vendor Defined Page 1)
   0x09, 0x01,                         // USAGE (Vendor Usage 1)
   0xA1, 0x01,                         // COLLECTION (Application)
   0xC0                                // END_COLLECTION
};                                     // End of hid_report_descriptor
#define STR0LEN 4
code const BYTE String0Desc[STR0LEN] =
{
   STR0LEN, 0x03, 0x09, 0x04
};                                     // End of String0Desc
#define STR1LEN sizeof("SILICON LABORATORIES INC.")*2
code const BYTE String1Desc[STR1LEN] =
{
   STR1LEN, 0x03,
   'S', 0,
   'I', 0,
   'L', 0,
   'I', 0,
   'C', 0,
   'O', 0,
   'N', 0,
   ' ', 0,
   'L', 0,
   'A', 0,
   'B', 0,
   'O', 0,
   'R', 0,
   'A', 0,
   'T', 0,
   'O', 0,
   'R', 0,
   'I', 0,
   'E', 0,
   'S', 0,
   ' ', 0,
   'I', 0,
   'N', 0,
   'C', 0,
   '.', 0
  };                                   // End of String1Desc
#define STR2LEN sizeof("FW TEMPLATE   ")*2
code const BYTE String2Desc[STR2LEN] =
{
   STR2LEN, 0x03,
   'F', 0,
   'W', 0,
   ' ', 0,
   'T', 0,
   'E', 0,
   'M', 0,
   'P', 0,
   'L', 0,
   'A', 0,
   'T', 0,
   'E', 0,
   ' ', 0,
   ' ', 0,
   ' ', 0
};                                     // End of String2Desc
code const BYTE* StringDescTable[] =
{
   String0Desc,
   String1Desc,
   String2Desc
};
// These are response packets used for communication with host
code const BYTE ONES_PACKET[2] = {0x01, 0x00};
code const BYTE ZERO_PACKET[2] = {0x00, 0x00};
//-----------------------------------------------------------------------------
// End Of File
//-----------------------------------------------------------------------------