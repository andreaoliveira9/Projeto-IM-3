package Modalities;

import scxmlgen.interfaces.IOutput;

public enum Output implements IOutput {

    HELP_SEARCH_MUSIC("[FUSION][HELP][SEARCH_MUSIC]"),
    SEARCH_MUSIC("[FUSION][SEARCH_MUSIC]"),
    MOVEDOWN_RIGHT("[FUSION][MOVEDOWN_RIGHT]"),
    PUSH("[FUSION][PUSH]"),
    VOLUME_DOWN("[FUSION][VOLUME_DOWN]"),
    PAUSE("[FUSION][PAUSE]"),
    PLAY("[FUSION][PLAY]"),
    VOLUME_UP("[FUSION][VOLUME_UP]"),
    QUIT("[FUSION][QUIT]"),
    SELECT("[FUSION][SELECT]"),
    NEXT_TRACK("[FUSION][NEXT_TRACK]"),
    PREVIOUS_TRACK("[FUSION][PREVIOUS_TRACK]")

    ;

    private String event;

    Output(String m) {
        event = m;
    }

    public String getEvent() {
        return this.toString();
    }

    public String getEventName() {
        return event;
    }
}
