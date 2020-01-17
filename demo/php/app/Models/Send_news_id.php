<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Send_news_id extends Model
{
    protected $table = 'send_news_ids';
    protected $fillable = ['cwxid','newsid'];
}
