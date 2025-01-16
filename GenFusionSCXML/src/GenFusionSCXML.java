/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import scxmlgen.Fusion.FusionGenerator;
//import FusionGenerator;

import Modalities.Output;
import Modalities.Speech;
import Modalities.Gestures;

/**
 *
 * @author nunof
 */
public class GenFusionSCXML {

  /**
   * @param args the command line arguments
   */
  public static void main(String[] args) throws IOException {

    FusionGenerator fg = new FusionGenerator();

    fg.Complementary(Gestures.SCRATCHHEAD, Speech.HELP_SEARCH_MUSIC, Output.HELP_SEARCH_MUSIC);
    fg.Complementary(Gestures.EARHAND, Speech.VOLUME_UP, Output.VOLUME_UP);
    fg.Complementary(Gestures.PUSH, Speech.PAUSE, Output.PAUSE);
    fg.Complementary(Gestures.PUSH, Speech.PLAY, Output.PLAY);
    fg.Complementary(Gestures.PUSH, Speech.SELECT, Output.SELECT);
    fg.Complementary(Gestures.ARMSX, Speech.QUIT, Output.QUIT);

    fg.Single(Gestures.EARHAND, Output.EARHAND);
    fg.Single(Gestures.SCRATCHHEAD, Output.SCRATCHHEAD);
    fg.Single(Gestures.MOVERIGHT, Output.MOVERIGHT);
    fg.Single(Gestures.MOVELEFT, Output.MOVELEFT);
    fg.Single(Gestures.MOVEDOWN_RIGHT, Output.MOVEDOWN_RIGHT);
    fg.Single(Gestures.MOVEUP_RIGHT, Output.MOVEUP_RIGHT);

    fg.Redundancy(Gestures.MOVERIGHT, Speech.NEXT_TRACK, Output.NEXT_TRACK);
    fg.Redundancy(Gestures.MOVELEFT, Speech.PREVIOUS_TRACK, Output.PREVIOUS_TRACK);

    fg.Build("fusion.scxml");

  }

}
