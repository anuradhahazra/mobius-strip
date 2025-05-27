from mobius_strip import MobiusStrip

def get_input(prompt, cast_type, default):
    try:
        value = input(prompt)
        return cast_type(value) if value else default
    except ValueError:
        print(f"Invalid input. Using default: {default}")
        return default

if __name__ == "__main__":
    print("🔷 Mobius Strip Parameters 🔷")

    R = get_input("Enter Radius R (default 1.0): ", float, 1.0)
    w = get_input("Enter Width w (default 0.3): ", float, 0.3)
    n = get_input("Enter Resolution n (default 300): ", int, 300)

    mobius = MobiusStrip(R=R, w=w, n=n)

    area = mobius.compute_surface_area()
    edge = mobius.compute_edge_length()

    print(f"\nSurface Area ≈ {area:.5f}")
    print(f"Edge Length ≈ {edge:.5f}")

    mobius.plot(save=True)
