import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML
from tempfile import NamedTemporaryFile
import base64

def run_animation(anim_frames):
    VIDEO_TAG = """
    <video controls>
        <source type="video/mp4"src="data:video/mp4;base64,{0}">
    </video>
    """

    db, pd, _ = anim_frames[0]
    db_x = np.linspace(-8, 8, len(db))
    p_x = np.linspace(-8, 8, len(pd))

    def anim_to_html(anim):
        with NamedTemporaryFile(suffix='.mp4') as f:
            anim.save(f.name, fps=20, extra_args=['-vcodec', 'libx264', '-pix_fmt', 'yuv420p'])
            video = open(f.name, 'rb').read()
        anim._encoded_video = base64.b64encode(video).decode('ascii')
        return VIDEO_TAG.format(anim._encoded_video)

    def init():
        line_db.set_data([], [])
        line_pd.set_data([], [])
        line_pg.set_data([], [])
        frame_number.set_text('')
        return line_db, line_pd, line_pg

    def animate(i):
        frame_number.set_text('Frame: %d/%d' % (i + 1, len(anim_frames)))

        db, pd, pg = anim_frames[i]
        line_db.set_data(db_x, db)
        line_pd.set_data(p_x, pd)
        line_pg.set_data(p_x, pg)
        return line_db, line_pd, line_pg

    fig = plt.figure()
    ax = plt.axes(xlim=(-8, 8), ylim=(0, 1.0))
    line_db, = ax.plot([], [], label='decision boundary')
    line_pd, = ax.plot([], [], label='real data')
    line_pg, = ax.plot([], [], label='generated data')
    frame_number = ax.text(0.02, 0.95, '', horizontalalignment='left',
                           verticalalignment='top', transform=ax.transAxes)

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=len(anim_frames), blit=True)

    html = HTML(anim_to_html(anim))
    plt.close(anim._fig)
    return html
