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
    NEXT_TRACK("[GESTURES][MOVERIGHT]"),
    PREVIOUS_TRACK("[GESTURES][MOVELEFT]"),
    SCRATCHHEAD("[GESTURES][SCRATCHHEAD]"),
    EARHAND("[GESTURES][EARHAND]"),
    MOVEUP_RIGHT("[FUSION][MOVEUP_RIGHT]"),

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
