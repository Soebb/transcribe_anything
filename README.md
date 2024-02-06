
# transcribe-anything
Input a local file or url and this service will transcribe it using Mozilla Deepspeech 0.9.3.

# Build Status

[![Actions Status](https://github.com/zackees/transcribe-anything/workflows/MacOS_Tests/badge.svg)](https://github.com/zackees/transcribe-anything/actions/workflows/push_macos.yml)
[![Actions Status](https://github.com/zackees/transcribe-anything/workflows/Win_Tests/badge.svg)](https://github.com/zackees/transcribe-anything/actions/workflows/push_win.yml)
[![Actions Status](https://github.com/zackees/transcribe-anything/workflows/Ubuntu_Tests/badge.svg)](https://github.com/zackees/transcribe-anything/actions/workflows/push_ubuntu.yml)


# Example

  * Example (cmd):
    * `transcribe_anything <YOUTUBE_URL> > out_subtitles.txt`
    * `transcribe_anything <LOCAL.MP4/WAV> > out_subtitles.txt`
  * Example (api):
    ```
    from transcribe_anything.api import bulk_transcribe

    urls = ['https://www.youtube.com/watch?v=Erk4_jFDjzQ']
    def onresolve(url, sub): print(url, sub)
    def onfail(url): print(f'Failed: {url}')
    bulk_transcribe(urls, onresolve=onresolve, onfail=onfail)
    ```


## Required: Install to current python environment
  * `pip install https://github.com/Soebb/transcribe_anything/archive/main.zip`
    * The command `transcribe_anything` will magically become available.
  * `transcribe_anything <YOUTUBE_URL> > out_subtitles.txt`
  * -or- `transcribe_anything <MY_LOCAL.MP4/WAV> > out_subtitles.txt`

# How does it work?

This program performs fetching using YouTube-dl for downloading videos from video services, and then
stripping the audio track out.

[static_ffmpeg](https://pypi.org/project/static-ffmpeg/) is then called to transcode the audio track into a specific format that DeepSpeech requires.

Once the audio file has been prepared, [pydeepspeech](https://pypi.org/project/pydeepspeech/) is called. This little
utility automatically downloads the proper AI models and installs them into the proper path so that deepspeech can be
called. It also partitions the input wav file into chunks, split at the parts of silence, in order to make processing
go easier (DeepSpeech degrades performance significantly with longer audio clips, so they have to be kept short.)
