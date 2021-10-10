import tarfile
import h5py
from filelock import FileLock


def numerical_relativity_postmerger_waveform(**waveform_kwargs):

# <Start snip>

    tar_location = waveform_kwargs['nr_tar_path']
    filename = waveform_kwargs['filename']
    loudness = waveform_kwargs['loudness']

    t_0 = waveform_kwargs['t_0']

    if not tar_location.endswith('/'):
        tar_location += '/'

    lock = FileLock(LOCK_FILENAME)
    with lock:
        with tarfile.open(tar_location + filename, 'r') as tar:
            metadatalocn = tar.getmember(tar.getnames()[1])
            h5locn = tar.getmember(tar.getnames()[2])  # this is the location of the hdf5 portion of the tar
            h5locn.name = tar_location + h5locn.name
            tar.extract(h5locn)
            with h5py.File(h5locn.name, 'r') as f:
                rh22 = f['rh_22']
                keys = list(rh22.keys())
                h22furthest = [key for key in keys if ('Rh_l2_m2' in key) and not ('Inf' in key)][-1]
                rh22data = rh22[h22furthest]
# <End snip>            
