package Modalities;

import scxmlgen.interfaces.IModality;

public enum Gestures implements IModality {
  // Gestures
  SCRATCHHEAD("[GESTURES][SCRATCHHEAD]", 5000),
  MOVEDOWN_RIGHT("[GESTURES][MOVEDOWNR]", 5000),
  PUSH("[GESTURES][PUSH]", 5000),
  EARHAND("[GESTURES][EARHAND]", 5000),
  ARMSX("[GESTURES][ARMSX]", 5000),
  MOVERIGHT("[GESTURES][MOVERIGHT]", 5000),
  MOVELEFT("[GESTURES][MOVELEFT]", 5000),
  MOVEUP_RIGHT("[GESTURES][MOVEUPR]", 5000);

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
