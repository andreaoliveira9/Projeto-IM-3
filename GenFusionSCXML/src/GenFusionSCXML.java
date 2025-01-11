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

    fg.Single(Speech.SEARCH_MUSIC, Output.SEARCH_MUSIC);
    fg.Single(Gestures.MOVEDOWN_RIGHT, Output.MOVEDOWN_RIGHT);
    fg.Single(Gestures.PUSH, Output.PUSH);
    fg.Single(Speech.VOLUME_DOWN, Output.VOLUME_DOWN);

    fg.Redundancy(Gestures.PUSH, Speech.PAUSE, Output.PAUSE);
    fg.Redundancy(Gestures.PUSH, Speech.PLAY, Output.PLAY);
    fg.Redundancy(Gestures.ARMSX, Speech.QUIT, Output.QUIT);

    fg.Build("fusion_novo.scxml");

  }

}
