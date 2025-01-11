package Modalities;

import scxmlgen.interfaces.IModality;

public enum Gestures implements IModality {
  // Gestures
  SCRATCHHEAD("[GESTURES][SCRATCHHEAD]", 1500),
  MOVEDOWN_RIGHT("[GESTURES][MOVEDOWN_RIGHT]", 1500),
  PUSH("[GESTURES][PUSH]", 1500),
  EARHAND("[GESTURES][EARHAND]", 1500),
  ARMSX("[GESTURES][ARMSX]", 1500),

  ;

  private String event;
  private int timeout;

  Gestures(String m, int time) {
    event = m;
    timeout = time;
  }

  @Override
  public int getTimeOut() {
    return timeout;
  }

  @Override
  public String getEventName() {
    // return getModalityName()+"."+event;
    return event;
  }

  @Override
  public String getEvName() {
    return getModalityName().toLowerCase() + event.toLowerCase();
  }

}
