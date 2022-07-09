#ifdef ENCODER_ENABLE
bool encoder_update_kb(uint8_t index, bool clockwise) {
    if (!encoder_update_user(index, clockwise)) {
        return false;
    }
    if (clockwise) {
        tap_code_delay(KC_VOLU, 10);
    } else {
        tap_code_delay(KC_VOLD, 10);
    }
    return false;
}
#endif

#ifdef OLED_ENABLE
void render_oled(void) {
    static const char display_item[] PROGMEM ={
        //INSERT ITEM HERE
        };
    oled_write_P(display_item false);
}

bool oled_task_kb(void) {
    if (oled_task_user()) {
        oled_write_P(led_state.num_lock ? PSTR("NUMLOCK") : PSTR("       "), false);
        oled_write_P(led_state.caps_lock ? PSTR("CAPS") : PSTR("    "), false);
        oled_write_P(led_state.scroll_lock ? PSTR("SCLK") : PSTR("    "), false);
        oled_advance_page(true);
        render_oled();
    }
    return false;
}
#endif