from typing import Dict, List, Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config


def start_panel(strings: Dict[str, str]) -> InlineKeyboardMarkup:
    """
    Generate start menu buttons
    """
    buttons = [
        [
            InlineKeyboardButton(
                text=strings["S_B_1"],
                url=f"https://t.me/{config.BOT_USERNAME}?startgroup=true",
            ),
            InlineKeyboardButton(
                text=strings["S_B_2"], url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                text=strings["S_B_3"], url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text=strings["S_B_4"], callback_data="settings_helper"
            ),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def help_panel(strings: Dict[str, str]) -> InlineKeyboardMarkup:
    """
    Generate help menu buttons
    """
    buttons = [
        [
            InlineKeyboardButton(
                text=strings["H_B_1"], callback_data="help_music"
            ),
            InlineKeyboardButton(
                text=strings["H_B_2"], callback_data="help_admin"
            ),
        ],
        [
            InlineKeyboardButton(
                text=strings["H_B_3"], callback_data="help_sudo"
            ),
            InlineKeyboardButton(
                text=strings["H_B_4"], callback_data="help_owner"
            ),
        ],
        [
            InlineKeyboardButton(
                text=strings["H_B_5"], callback_data="help_tools"
            ),
        ],
        [
            InlineKeyboardButton(
                text=strings["S_B_6"], url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text=strings["S_B_7"], callback_data="start_command"
            ),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def stream_markup(_, videoid: str, chat_id: int) -> InlineKeyboardMarkup:
    """
    Stream inline buttons for playback control
    """
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏸", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="⏭", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="⏹", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="🎵 Support Channel",
                url=config.SUPPORT_CHANNEL,
            ),
            InlineKeyboardButton(
                text="📁 Source", url=f"https://t.me/SANATANI_TECH"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔄 Close", callback_data=f"close"
            )
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def track_markup(_, videoid, user_id, channel, fplay) -> InlineKeyboardMarkup:
    """
    Track selection buttons
    """
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def playlist_markup(_, videoid, user_id, ptype, channel, fplay) -> InlineKeyboardMarkup:
    """
    Playlist selection buttons
    """
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"ProfessorPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"ProfessorPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def setting_markup(strings: Dict[str, str]) -> InlineKeyboardMarkup:
    """
    Settings panel buttons
    """
    buttons = [
        [
            InlineKeyboardButton(text=strings["ST_B_1"], callback_data="AQ"),
            InlineKeyboardButton(text=strings["ST_B_2"], callback_data="VQ"),
        ],
        [
            InlineKeyboardButton(text=strings["ST_B_3"], callback_data="AU"),
            InlineKeyboardButton(text=strings["ST_B_4"], callback_data="VM"),
        ],
        [
            InlineKeyboardButton(text=strings["ST_B_5"], callback_data="LG"),
        ],
        [
            InlineKeyboardButton(text=strings["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def language_markup(strings: Dict[str, str], keyboard: List) -> InlineKeyboardMarkup:
    """
    Language selection buttons
    """
    buttons = keyboard
    buttons.append(
        [
            InlineKeyboardButton(
                text=strings["BACK_BUTTON"],
                callback_data="settings_helper",
            ),
            InlineKeyboardButton(
                text=strings["CLOSE_BUTTON"], callback_data="close"
            ),
        ]
    )
    return InlineKeyboardMarkup(buttons)


def auth_users_markup(_, status: str) -> InlineKeyboardMarkup:
    """
    Auth users setting buttons
    """
    buttons = [
        [
            InlineKeyboardButton(text="👥 Everyone", callback_data="PERM_AUTH everyone"),
            InlineKeyboardButton(text="🧑‍✈️ Admins", callback_data="PERM_AUTH admin"),
        ],
        [
            InlineKeyboardButton(
                text="📝 Permission Lists", callback_data="PERM_AUTH list"
            ),
        ],
        [
            InlineKeyboardButton(text="🔄 Back", callback_data="settings_helper"),
            InlineKeyboardButton(text="❌ Close", callback_data="close"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def confirm_markup(_, videoid, user_id, action) -> InlineKeyboardMarkup:
    """
    Confirmation buttons
    """
    buttons = [
        [
            InlineKeyboardButton(
                text=_["YES_BUTTON"],
                callback_data=f"confirm {action}|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text=_["NO_BUTTON"],
                callback_data=f"confirm NO|{videoid}|{user_id}",
            ),
        ],
    ]
    return InlineKeyboardMarkup(buttons)
