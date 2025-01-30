

## Temp


    onViewStateChange: ({ viewState }) => {
                // only if mouse is currently hovering over this decks container #deckGLContainer1 (and NOT the other deck)
                if (hoveringElement === "deck1") {
                    syncZoomAndPan(viewState, deck2);
                }
            }

          function syncZoomAndPan(viewState, deckToChange) {
            deckToChange.setProps({
                viewState: viewState
            });
        }