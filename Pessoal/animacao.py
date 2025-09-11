from manim import *

def arc(a, b, calls=None, depth=0, parent=None):
    """
    Função recursiva arc que também registra chamadas para visualização.
    """
    if calls is None:
        calls = []

    current_index = len(calls)
    calls.append((a, b, depth, parent))

    if a == 0:
        return b + 1
    elif b == 0:
        return arc(a - 1, 1, calls, depth + 1, current_index)
    else:
        return arc(a - 1, arc(a, b - 1, calls, depth + 1, current_index), calls, depth + 1, current_index)


class ArcRecursionTree(MovingCameraScene):
    def construct(self):
        calls = []
        result = arc(2, 10, calls)

        # Cria os nós (todos começam no topo da tela)
        nodes = [Text(f"arc({a},{b})", font_size=28).move_to(UP * 3) for (a, b, _, _) in calls]

        # Posições finais dos nós
        final_positions = {}
        layers = {}
        for i, (a, b, depth, parent) in enumerate(calls):
            if depth not in layers:
                layers[depth] = []
            layers[depth].append(i)

        for depth, indices in layers.items():
            for j, i in enumerate(indices):
                # Distâncias reduzidas para caber na tela
                final_positions[i] = RIGHT * (j - len(indices)/2) * 1.5 + DOWN * depth * 1.0

        # Setas
        arrows = {}
        for i, (a, b, depth, parent) in enumerate(calls):
            if parent is not None:
                arrows[i] = Arrow(
                    start=final_positions[parent] + DOWN * 0.3,
                    end=final_positions[i] + UP * 0.3,
                    buff=0.2,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.1
                )

        # Anima: nó desce do topo -> seta aparece -> câmera acompanha
        for i, node in enumerate(nodes):
            self.play(node.animate.move_to(final_positions[i]), run_time=0.6)
            # câmera segue o nó
            self.play(self.camera.frame.animate.move_to(node.get_center() + DOWN*0.5), run_time=0.5)
            if i in arrows:
                self.play(GrowArrow(arrows[i]), run_time=0.4)

        # Retornos em ordem inversa
        for i in reversed(range(len(nodes))):
            if i in arrows:
                self.play(FadeOut(arrows[i]), run_time=0.3)
            self.play(nodes[i].animate.set_color(YELLOW), run_time=0.2)

        # Resultado final
        result_text = Text(f"Resultado final: {result}", font_size=32, color=GREEN)
        result_text.to_edge(DOWN)
        self.play(Write(result_text))
        self.wait(2)
