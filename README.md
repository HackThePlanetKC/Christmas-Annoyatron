Roadmap:

1: Create diagram for RGB LED installation in standard Christmas ornament size. Probably WS2812B strip. I do have 100x 5mm 2 pin RGB LEDs, might use those instead, will test.
  Note: Those 5mm auto cycle, very simple, might use those
  Also needs spot for active buzzer, Trinket M0 board, 600 mAh, Trinket LiPo backpack
2: Code:
  Main Loop:
    1 week init delay
    random whole int 1-7
    Delay for int
    0.5 sec high pitch buzz

  Second loop:
    Button press toggles light on/off, doesn't effect main loop 
